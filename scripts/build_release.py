"""Build a deterministic, self-contained installable ZIP and SHA256 sidecar."""
import argparse
import hashlib
from pathlib import Path
import re
import zipfile

from validate_skill import ROOT, validate


def build(version, output_dir=None, root=ROOT):
    if not re.fullmatch(r'v\d+\.\d+\.\d+(?:-[0-9A-Za-z]+(?:[.-][0-9A-Za-z]+)*)?', version):
        raise ValueError('Version must be vMAJOR.MINOR.PATCH with optional prerelease suffix')
    entries = validate(root)
    output = Path(output_dir) if output_dir is not None else root / 'dist'
    output.mkdir(parents=True, exist_ok=True)
    archive = output / f'project-kickoff-{version}.zip'
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as bundle:
        for entry in sorted(entries):
            info = zipfile.ZipInfo(f'project-kickoff/{entry}', date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, (root / entry).read_bytes())
    checksum = archive.with_suffix('.zip.sha256')
    checksum.write_text(f'{hashlib.sha256(archive.read_bytes()).hexdigest()}  {archive.name}\n', encoding='ascii')
    with zipfile.ZipFile(archive) as bundle:
        if bundle.testzip() is not None:
            raise ValueError('ZIP integrity verification failed')
        for entry in entries:
            if bundle.read(f'project-kickoff/{entry}') != (root / entry).read_bytes():
                raise ValueError(f'Archived resource mismatch: {entry}')
    print(archive)
    print(checksum)
    return archive, checksum


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--version', required=True)
    parser.add_argument('--output-dir', type=Path)
    args = parser.parse_args()
    build(args.version, args.output_dir)
