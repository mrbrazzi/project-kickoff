import hashlib
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from build_release import build
from validate_skill import runtime_files


class ReleaseTests(unittest.TestCase):
    def test_workflows_use_repository_tooling_and_tag_scoped_release(self):
        import yaml
        ci = yaml.load((ROOT / '.github/workflows/ci.yml').read_text(), Loader=yaml.BaseLoader)
        release = yaml.load((ROOT / '.github/workflows/release.yml').read_text(), Loader=yaml.BaseLoader)
        self.assertIn('pull_request', ci['on'])
        self.assertEqual(release['on']['push']['tags'], ['v*'])
        self.assertEqual(release['jobs']['release']['permissions']['contents'], 'write')
        for workflow, job in ((ci, 'validate'), (release, 'release')):
            commands = '\n'.join(step.get('run', '') for step in workflow['jobs'][job]['steps'])
            self.assertIn('python scripts/validate_skill.py', commands)
            self.assertIn('python -m unittest discover -s tests -v', commands)
            self.assertIn('python scripts/build_release.py', commands)
        publish = release['jobs']['release']['steps'][-1]
        self.assertEqual(publish['env']['RELEASE_TAG'], '${{ github.ref_name }}')
        self.assertIn('--verify-tag', publish['run'])
        self.assertIn('.zip.sha256', publish['run'])

    def test_extracted_package_is_complete_and_self_contained(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp)
            archive, checksum = build('v1.0.0', output)
            expected = runtime_files()
            with zipfile.ZipFile(archive) as bundle:
                self.assertEqual(set(bundle.namelist()), {f'project-kickoff/{e}' for e in expected})
                bundle.extractall(output / 'install')
            installed = output / 'install/project-kickoff'
            for entry in expected:
                self.assertEqual((installed / entry).read_bytes(), (ROOT / entry).read_bytes())
            self.assertEqual(checksum.read_text().split()[0], hashlib.sha256(archive.read_bytes()).hexdigest())
            self.assertFalse((installed / '.git').exists())
            self.assertFalse((installed / 'tests').exists())
            self.assertFalse((installed / 'scripts').exists())
            import re
            for link in re.findall(r'\]\(((?:assets|references)/[^)]+)\)', (installed / 'SKILL.md').read_text()):
                self.assertTrue((installed / link).is_file())

    def test_same_inputs_produce_same_zip(self):
        with tempfile.TemporaryDirectory() as temp:
            first, _ = build('v1.2.3-rc.1', Path(temp) / 'a')
            second, _ = build('v1.2.3-rc.1', Path(temp) / 'b')
            self.assertEqual(first.read_bytes(), second.read_bytes())

    def test_unsafe_version_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            for version in ('../escape', 'v1.0', 'v1.0.0/extra'):
                with self.subTest(version=version), self.assertRaises(ValueError):
                    build(version, Path(temp))
            self.assertEqual(list(Path(temp).iterdir()), [])

    def test_manifest_cannot_escape_root_or_include_missing_resource(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for entry in ('../outside', '/absolute', 'missing.md', 'SKILL.md\nSKILL.md'):
                (root / 'release-manifest.txt').write_text(entry)
                with self.subTest(entry=entry), self.assertRaises(ValueError):
                    runtime_files(root)

    def test_both_design_locales_share_machine_readable_contract(self):
        from validate_skill import frontmatter
        designs = [frontmatter((ROOT / f'assets/{locale}/DESIGN.template.md').read_text(encoding='utf-8')) for locale in ('en', 'es')]
        self.assertEqual(set(designs[0]), set(designs[1]))
        self.assertEqual(designs[0]['colors'], designs[1]['colors'])


if __name__ == '__main__':
    unittest.main()
