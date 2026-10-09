# Comprobación e instalación de dependencias

## Git

Comprueba disponibilidad y ejecución, no solo presencia en PATH:

| Entorno | Localizar | Verificar |
| --- | --- | --- |
| Windows / PowerShell | `Get-Command git -ErrorAction SilentlyContinue` | `git --version` |
| macOS / Linux / WSL | `command -v git` | `git --version` |

Un Git instalado fuera de PATH puede necesitar una nueva sesión o una ruta absoluta.
Un error de ejecución merece diagnóstico antes de proponer otra instalación. Detecta
el sistema donde se ejecutará el proyecto: Git de Windows y Git de WSL son entornos
distintos. No instales en ambos sin necesidad.

Si falta, explica que Git registra versiones y permite revisar o recuperar cambios.
Propón el método disponible y pide permiso antes de descargar o instalar. Consulta
las [instrucciones oficiales](https://git-scm.com/install/) vigentes. En Windows,
puede usarse el paquete exacto `Git.Git` con winget si existe; en macOS, un gestor ya
instalado o las herramientas del sistema; en Linux, el gestor de la distribución.
No instales un gestor adicional ni uses privilegios administrativos sin aprobación.
No ejecutes scripts remotos sin revisarlos. Verifica el comando y su código de salida
después de instalar, respetando el entorno y las aprobaciones del host.

## Engram

Fuentes mantenidas:

- [Repositorio oficial](https://github.com/Gentleman-Programming/engram).
- [Instalación](https://github.com/Gentleman-Programming/engram/blob/main/docs/INSTALLATION.md).
- [Configuración de agentes](https://github.com/Gentleman-Programming/engram/blob/main/docs/AGENT-SETUP.md).

Consulta estas fuentes cuando vayas a instalar o registrar un cliente; no fijes una
versión, un nombre de recurso o una ruta de módulo de Go de memoria. Selecciona una
versión estable compatible y explica los componentes necesarios antes de pedir
autorización. La instalación del binario y la configuración del cliente MCP son
acciones diferentes; informa si queda pendiente reiniciar el cliente para conectar.

Orden de diagnóstico:

1. Descubre herramientas MCP de Engram mediante el mecanismo del agente. Una lectura
   exitosa, como `mem_current_project` según el esquema vivo, prueba acceso al backend.
   Verifica que la ruta identificada corresponde al proyecto antes de escribir.
2. Si no hay conexión, localiza `engram` en el entorno activo con `Get-Command` o
   `command -v`. Consulta `engram version` y, si hace falta, `engram --help`.
3. Si hay evidencia de integración en WSL, contenedor o servicio, revisa únicamente
   su estado y el launcher pertinente. No inspecciones credenciales, volúmenes o
   todas las distribuciones indiscriminadamente. No interpretes un backend detenido
   bajo demanda como desinstalado.
4. Con metadatos pero sin ejecución verificable, informa «instalación/configuración
   detectada; acceso no verificado». Si no puedes comprobar otros entornos, informa
   la incertidumbre y pide al usuario su ubicación en lugar de instalar duplicados.

Engram conserva conocimiento entre sesiones; Git conserva versiones de archivos.
Su uso opcional no sustituye README.md ni AGENTS.md. La presencia de una skill de
Engram tampoco equivale a un backend operativo.

Si el usuario autoriza instalar, usa el método oficial apropiado al entorno y
comprueba integridad del paquete cuando existan checksums. Conserva cualquier
instalación o configuración previa y no migres datos automáticamente. En entornos
con integración de Engram ya aprobada, puedes aprovechar su skill especializada
si está disponible; esta skill debe funcionar también sin ella.

Verifica binario o servicio tras instalar y, por separado, acceso del agente.
Documenta dónde reside la memoria y si el cliente necesita reconexión. No guardes
secretos ni contenido completo del proyecto. Ante un fallo, reporta el error y
continúa con Git y documentos sin reinstalar ni reparar a ciegas.
