# Instrucciones para Claude Code — Ajuste de tono: reducir sobreexposición de Victor

> Proyecto: `\\wsl.localhost\Ubuntu-24.04\home\victor\landing-guaranisoft`
> Archivo a editar: `templates/index.html` (4 cambios)
> Objetivo: reducir menciones de Victor de 8 a 3 en la página de producto, proyectando equipo sin inventar personas.

---

## Cambio 1 — Pilares: "WhatsApp directo a Victor"

**BUSCAR en `templates/index.html`:**

```html
                    <h4>Soporte directo del que lo programó</h4>
                    <p>WhatsApp directo a Victor. Sin bots, sin call center, sin vueltas.</p>
```

**REEMPLAZAR por:**

```html
                    <h4>Soporte directo del que lo programó</h4>
                    <p>WhatsApp directo, sin bots ni call center. Nos escribís y te respondemos.</p>
```

**Por qué:** El diferenciador es el acceso sin intermediarios, no el nombre. "Nos escribís" implica equipo sin mentir.

---

## Cambio 2 — Botón "Hablar con Victor"

**BUSCAR en `templates/index.html`:**

```html
                    <a href="#contacto" class="btn btn-outline-morado btn-sm mt-3">Hablar con Victor</a>
```

**REEMPLAZAR por:**

```html
                    <a href="#contacto" class="btn btn-outline-morado btn-sm mt-3">Hablar con nosotros</a>
```

**Por qué:** "Hablar con Victor" suena a que siempre atiende la misma persona. "Hablar con nosotros" es más profesional y proyecta capacidad de respuesta.

---

## Cambio 3 — Tooltip del WhatsApp flotante

**BUSCAR en `templates/index.html`:**

```html
   title="¿Tenés dudas? Hablá directo con Victor" aria-label="Chatear por WhatsApp con Victor">
    <span class="whatsapp-float-tip" aria-hidden="true">¿Tenés dudas? Hablá directo con Victor</span>
```

**REEMPLAZAR por:**

```html
   title="¿Tenés dudas? Escribinos por WhatsApp" aria-label="Chatear por WhatsApp">
    <span class="whatsapp-float-tip" aria-hidden="true">¿Tenés dudas? Escribinos por WhatsApp</span>
```

**Por qué:** El tooltip aparece en cada página donde el usuario scrollea. Repetir "Victor" ahí es innecesario y genera la impresión de operación de una sola persona en cada interacción.

---

## Cambio 4 — Segundo párrafo de "¿Quién está detrás?"

**BUSCAR en `templates/index.html`:**

```html
                    <p class="mb-0">
                        Cuando comprás Ñande ERP, no estás comprando un producto de una empresa
                        anónima. Estás trabajando conmigo. Si algo no funciona, me escribís y lo
                        arreglo. Si necesitás una función nueva, la evaluamos juntos. Sin call
                        center, sin tickets, sin vueltas.
                    </p>
```

**REEMPLAZAR por:**

```html
                    <p class="mb-0">
                        Cuando elegís Ñande ERP, no estás comprando un producto de una empresa
                        anónima. Estás trabajando con quien lo construyó. Si algo no funciona,
                        lo resolvemos. Si necesitás una función nueva, la evaluamos juntos. Sin
                        call center, sin tickets, sin vueltas.
                    </p>
```

**Por qué:** Cambia "me escribís y lo arreglo" (una sola persona, riesgo de continuidad) por "lo resolvemos" (equipo, capacidad de respuesta). Mantiene la conexión personal del primer párrafo ("Soy Victor Román") pero el cierre proyecta escalabilidad.

---

## Resumen del impacto

| Ubicación | Antes | Después |
|-----------|-------|---------|
| Pilares | "WhatsApp directo a Victor" | "WhatsApp directo... nos escribís" |
| Botón CTA | "Hablar con Victor" | "Hablar con nosotros" |
| Tooltip flotante | "Hablá directo con Victor" ×2 | "Escribinos por WhatsApp" ×2 |
| Párrafo cierre | "me escribís y lo arreglo" | "lo resolvemos" |
| **Menciones "Victor" en producto** | **8** | **3** (foto, "Soy Victor Román", LinkedIn) |

Las 3 menciones que quedan son las correctas: la presentación personal (primer párrafo, que humaniza), la foto, y el link de LinkedIn. El resto usa "nosotros" o impersonal, proyectando equipo sin inventar personas que no existen.

## Después de aplicar

```bash
cd ~/landing-guaranisoft
source .venv/bin/activate
uvicorn main:app --reload
```

Verificar en `http://localhost:8000/nande-erp`:
1. El pilar "Soporte directo" ya no dice "Victor"
2. El botón dice "Hablar con nosotros"
3. El tooltip del WhatsApp flotante dice "Escribinos por WhatsApp"
4. El cierre de "¿Quién está detrás?" dice "lo resolvemos" en vez de "me escribís y lo arreglo"
5. La primera persona se mantiene solo en el primer párrafo ("Soy Victor Román")
