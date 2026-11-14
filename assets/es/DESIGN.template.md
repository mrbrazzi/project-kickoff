---
name: "{{Nombre de marca o proyecto}}"
category: "{{Categoría correspondiente al proyecto}}"
surface: "{{Superficie o medio confirmado; no asumir web}}"
colors:
  background: null
  surface: null
  foreground: null
  muted: null
  border: null
  accent: null
  accent-secondary: null
---

# {{Nombre de marca o proyecto}}

> Categoría: {{Categoría, coherente con el frontmatter}}

> Superficie: {{Superficie, coherente con el frontmatter}}

*{{Mensaje guía confirmado o propuesta identificada; omitir si no existe.}}*

{{Descripción breve contextual. Estado del documento: borrador/propuesta o aprobado.
Enlazar BRAND_IDENTITY.md si existe. Los tokens null indican decisiones pendientes;
sustituirlos por valores aprobados y reflejarlos también en la tabla.}}

## Paleta de colores

| Rol | Nombre | Hex | Uso |
| --- | --- | --- | --- |
| background | {{Nombre}} | {{Hex aprobado o Por decidir}} | {{Uso o No aplicable}} |
| surface | {{Nombre}} | {{Hex aprobado o Por decidir}} | {{Uso o No aplicable}} |
| foreground | {{Nombre}} | {{Hex aprobado o Por decidir}} | {{Uso o No aplicable}} |
| muted | {{Nombre}} | {{Hex aprobado o Por decidir}} | {{Uso o No aplicable}} |
| border | {{Nombre}} | {{Hex aprobado o Por decidir}} | {{Uso o No aplicable}} |
| accent | {{Nombre}} | {{Hex aprobado o Por decidir}} | {{Uso o No aplicable}} |
| accent-secondary | {{Nombre}} | {{Hex aprobado o Por decidir}} | {{Uso o No aplicable}} |
| success | {{Nombre}} | {{Hex aprobado o Por decidir}} | {{Uso o No aplicable}} |
| warning | {{Nombre}} | {{Hex aprobado o Por decidir}} | {{Uso o No aplicable}} |

{{Adaptar roles a las superficies. Si success/warning se utilizan como tokens,
añadirlos también al mapa colors. No afirmar resultados de contraste medidos sin
evidencia; seguir la sección WCAG AA siguiente.}}

### Accesibilidad: contraste WCAG AA

**Requisito obligatorio para botones CTA:** todo botón de llamada a la acción
(primario, secundario o cualquier otra variante de CTA) debe cumplir WCAG 2.x nivel
AA en todos sus estados interactivos (reposo, hover, foco, activo/pulsado):

- **Texto de la etiqueta frente al fondo del CTA:** al menos 4.5:1 (CE 1.4.3);
  3:1 solo si la etiqueta es texto grande (≥ 24 px regular o ≥ 18.66 px en negrita,
  o su equivalente en la superficie).
- **Límite del CTA frente al fondo adyacente:** al menos 3:1 cuando la forma del
  botón se transmite mediante su relleno o borde (CE 1.4.11).
- **Indicador de foco:** visible y con al menos 3:1 frente a los colores adyacentes
  (CE 1.4.11).
- Una combinación de colores de CTA que no cumpla AA no puede aprobarse ni usarse;
  queda marcada como decisión pendiente hasta que se apruebe una alternativa conforme.

**Evaluación proactiva de la paleta (instrucción para el agente de IA):** en cuanto
se defina la paleta o cambie cualquier color, y antes de marcarla como aprobada, el
agente debe, sin esperar a que se lo pidan:

1. Calcular la relación de contraste WCAG de cada par relevante: `foreground` y
   `muted` sobre `background` y `surface`; etiqueta del CTA sobre `accent` y
   `accent-secondary` (y sobre el color de cada estado); `accent`/`accent-secondary`
   frente a `background`/`surface` para UI no textual; `border` cuando sea el único
   indicador de un componente; `success`/`warning` con el texto que acompañen.
2. Registrar los resultados en la tabla siguiente con la relación medida, el umbral
   exigido y el resultado (cumple AA / no cumple AA). Informar solo valores
   calculados; nunca estimarlos.
3. Presentar al usuario un resumen general del cumplimiento WCAG AA, destacando cada
   incumplimiento (primero los de CTA) y proponiendo opciones concretas de corrección
   para cada uno (p. ej., oscurecer/aclarar un tono indicando su nuevo hex y relación,
   cambiar el color de la etiqueta, limitar el par a texto grande o uso decorativo,
   añadir un borde).
4. Consultar explícitamente al usuario qué acciones aprobar o tomar para cada
   hallazgo (aplicar la corrección propuesta, elegir otra alternativa, aceptar una
   excepción documentada para usos que no sean CTA o dejarlo pendiente). No cambiar
   colores aprobados ni marcar la paleta como aprobada sin esa confirmación. Los
   incumplimientos de CTA no pueden aceptarse como excepción.
5. Actualizar la paleta, el frontmatter `colors` y esta tabla con las decisiones
   aprobadas, y repetir la evaluación si cambia algún color.

| Par (primer plano / fondo) | Uso | Relación | AA exigido | Resultado | Acción aprobada |
| --- | --- | --- | --- | --- | --- |
| {{p. ej., etiqueta CTA / accent}} | {{CTA primario}} | {{Relación calculada o Pendiente}} | {{4.5:1 / 3:1}} | {{Cumple AA / No cumple AA / Pendiente}} | {{Decisión confirmada por el usuario o Pendiente}} |
| {{p. ej., foreground / background}} | {{Texto de cuerpo}} | {{Relación calculada o Pendiente}} | {{4.5:1}} | {{Cumple AA / No cumple AA / Pendiente}} | {{Decisión confirmada por el usuario o Pendiente}} |

## Tipografía

- **Titulares:** {{Familia, pesos y fallbacks aprobados o decisiones pendientes.}}
- **Cuerpo:** {{Familia, pesos y fallbacks aprobados o decisiones pendientes.}}

## Voz y tono

- **Adjetivos:** {{Rasgos de la marca confirmados.}}
- **Tono:** {{Regla operativa y adaptación al contexto.}}

### Pilares de comunicación

{{Mensajes clave coherentes con BRAND_IDENTITY.md cuando exista; marcar propuestas.}}

### Vocabulario

- **Usar:** {{Vocabulario recomendado.}}
- **Evitar:** {{Expresiones que deben evitarse.}}

## Imágenes

- **Estilo:** {{Estilo o criterios visuales; no imponer una estética.}}
- **Sujetos:** {{Sujetos pertinentes, sin inventar personas o activos existentes.}}
- **Tratamiento:** {{Dirección de arte y tratamiento.}}
- **Evitar:** {{Exclusiones acordadas.}}

## Composición

- **Radio:** {{Valor con unidad o Por decidir/No aplicable.}}
- **Grosor de borde:** {{Valor con unidad o Por decidir/No aplicable.}}
- **Espaciado:** {{Sistema y unidades según la superficie o Por decidir.}}

### Reglas de composición

{{Reglas de densidad, jerarquía, composición y comportamiento para las superficies
elegidas. No asumir tarjetas, glassmorphism, modo oscuro o animaciones. Indicar
decisiones pendientes y cómo validarlas.}}
