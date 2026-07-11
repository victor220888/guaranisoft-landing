# Instrucciones para Claude Code — Reescritura de "Quiénes somos" y "¿Quién está detrás?"

> Proyecto: `\\wsl.localhost\Ubuntu-24.04\home\victor\landing-guaranisoft`
> Dos archivos a editar: `templates/home.html` y `templates/index.html`

---

## Cambio 1 — `templates/home.html` (página corporativa)

### Sección: "Quiénes somos"

**BUSCAR este bloque completo dentro de `home.html`:**

```html
                <div class="quien-texto">
                    <h3>Lic. Victor Román — Fundador</h3>
                    <p>
                        GuaraníSoft nace de más de 10 años de experiencia desarrollando
                        herramientas que brindan soluciones reales para empresas.
                        Trabajamos codo a codo con la realidad comercial de Paraguay:
                        Ley 6380/2019, RG 49/14, RESIMPLE y SIFEN.
                    </p>
                    <p class="mb-0">
                        Nuestro compromiso: software rápido, exacto y listo para cualquier
                        exigencia fiscal — con soporte directo de quien lo programa,
                        sin bots ni call centers.
                    </p>
                </div>
```

**REEMPLAZAR por:**

```html
                <div class="quien-texto">
                    <h3>Lic. Victor Román — Fundador</h3>
                    <p>
                        GuaraníSoft nació de una convicción simple: las PyMEs paraguayas
                        merecen software tan bueno como el de cualquier multinacional, pero
                        pensado para su realidad. Con más de 10 años desarrollando soluciones
                        locales, Victor entendió que el problema no era falta de sistemas —
                        era falta de sistemas que hablen el idioma del comerciante paraguayo.
                    </p>
                    <p>
                        Por eso construimos Ñande ERP: un sistema de gestión integral donde
                        el dueño del negocio controla sus ventas, su inventario y su
                        contabilidad desde un solo lugar — y con soporte directo, sin
                        intermediarios.
                    </p>
                    <p class="mb-0">
                        Hoy GuaraníSoft trabaja para que cada PyME que crece en Paraguay lo
                        haga con las cuentas claras y los impuestos al día.
                    </p>
                </div>
```

### Cambio adicional en `home.html` — agregar CTA al final de "Quiénes somos"

**BUSCAR:**

```html
                    <p class="mb-0">
                        Hoy GuaraníSoft trabaja para que cada PyME que crece en Paraguay lo
                        haga con las cuentas claras y los impuestos al día.
                    </p>
                </div>
```

**REEMPLAZAR por:**

```html
                    <p class="mb-0">
                        Hoy GuaraníSoft trabaja para que cada PyME que crece en Paraguay lo
                        haga con las cuentas claras y los impuestos al día.
                    </p>
                    <a href="/nande-erp" class="btn btn-outline-morado btn-sm mt-3">Conocé Ñande ERP</a>
                </div>
```

> ⚠️ **Nota:** El link `/nande-erp` NO debe llevar `target="_blank"`. Es navegación interna del mismo sitio.

---

## Cambio 2 — `templates/index.html` (página de producto)

### Sección: "¿Quién está detrás?"

**BUSCAR este bloque completo dentro de `index.html`:**

```html
                <div class="quien-texto">
                    <h3 id="quien-heading">¿Quién está detrás?</h3>
                    <p>
                        Soy <strong>Lic. Victor Román</strong>, desarrollador paraguayo con más de 10 años
                        de experiencia en el mercado, creando herramientas que brindan soluciones reales
                        para empresas. Construí Ñande ERP desde cero, trabajando codo a codo con la
                        realidad comercial de Paraguay: Ley 6380/2019, RG 49/14, RESIMPLE y SIFEN v150.
                    </p>
                    <p class="mb-0">
                        Mi compromiso es darte una herramienta rapidísima para tu mostrador, y la
                        tranquilidad de que tu inventario, tu caja y tu contabilidad están exactos y
                        listos para cualquier exigencia fiscal. Cuando trabajás conmigo, le hablás
                        directo al que programa el sistema.
                    </p>
                    <a href="#contacto" class="btn btn-outline-morado btn-sm mt-3">Hablar con Victor</a>
                </div>
```

**REEMPLAZAR por:**

```html
                <div class="quien-texto">
                    <h3 id="quien-heading">¿Quién está detrás?</h3>
                    <p>
                        Soy <strong>Victor Román</strong>, el que programó Ñande ERP. Llevo más de
                        10 años escribiendo software para empresas, pero este sistema lo construí
                        trabajando directo con comerciantes: escuchando qué les frena, qué les
                        hace perder plata, qué les complica el día.
                    </p>
                    <p class="mb-0">
                        Cuando comprás Ñande ERP, no estás comprando un producto de una empresa
                        anónima. Estás trabajando conmigo. Si algo no funciona, me escribís y lo
                        arreglo. Si necesitás una función nueva, la evaluamos juntos. Sin call
                        center, sin tickets, sin vueltas.
                    </p>
                    <a href="#contacto" class="btn btn-outline-morado btn-sm mt-3">Hablar con Victor</a>
                </div>
```

---

## Cambio 3 — `templates/index.html` (página de producto)

### Eliminar `target="_blank"` de los links internos entre páginas

**BUSCAR en `index.html`:**

```html
<li class="nav-item"><a class="nav-link corp-nav-link" href="/" target="_blank" rel="noopener">Guaraní<span>Soft</span></a></li>
```

**REEMPLAZAR por:**

```html
<li class="nav-item"><a class="nav-link corp-nav-link" href="/">Guaraní<span>Soft</span></a></li>
```

**BUSCAR en `index.html` (footer):**

```html
                <a href="/" target="_blank" rel="noopener">GuaraníSoft</a>
```

**REEMPLAZAR por:**

```html
                <a href="/">GuaraníSoft</a>
```

---

## Cambio 4 — `templates/home.html` (página corporativa)

### Eliminar `target="_blank"` de los links internos hacia /nande-erp

**BUSCAR en `home.html` (navbar):**

```html
                    <a href="/nande-erp" target="_blank" rel="noopener" class="btn btn-morado btn-sm">Conocé Ñande ERP</a>
```

**REEMPLAZAR por:**

```html
                    <a href="/nande-erp" class="btn btn-morado btn-sm">Conocé Ñande ERP</a>
```

**BUSCAR en `home.html` (hero):**

```html
            <a href="/nande-erp" target="_blank" rel="noopener" class="btn btn-morado">Conocé Ñande ERP</a>
```

**REEMPLAZAR por:**

```html
            <a href="/nande-erp" class="btn btn-morado">Conocé Ñande ERP</a>
```

**BUSCAR en `home.html` (sección producto, botón "Ver Ñande ERP"):**

```html
                <a href="/nande-erp" target="_blank" rel="noopener" class="btn btn-morado">Ver Ñande ERP</a>
```

**REEMPLAZAR por:**

```html
                <a href="/nande-erp" class="btn btn-morado">Ver Ñande ERP</a>
```

**BUSCAR en `home.html` (sección producto, botón "Solicitar demo"):**

```html
                <a href="/nande-erp#contacto" target="_blank" rel="noopener" class="btn btn-outline-morado">Solicitar demo</a>
```

**REEMPLAZAR por:**

```html
                <a href="/nande-erp#contacto" class="btn btn-outline-morado">Solicitar demo</a>
```

**BUSCAR en `home.html` (footer):**

```html
                <a href="/nande-erp" target="_blank" rel="noopener">Ñande ERP</a>
```

**REEMPLAZAR por:**

```html
                <a href="/nande-erp">Ñande ERP</a>
```

---

## Cambio 5 — `templates/home.html` (página corporativa)

### Agregar WhatsApp flotante antes del cierre de `</body>`

**BUSCAR en `home.html`:**

```html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
```

**INSERTAR ANTES de esa línea:**

```html
<!-- ═══ WhatsApp flotante ═══════════════════════════════════════════════ -->
<a href="https://wa.me/595992504620" target="_blank" rel="noopener" class="whatsapp-float"
   title="¿Tenés dudas? Hablá directo con Victor" aria-label="Chatear por WhatsApp con Victor">
    <span class="whatsapp-float-tip" aria-hidden="true">¿Tenés dudas? Hablá directo con Victor</span>
    <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51l-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>
</a>

```

---

## Cambio 6 — `static/css/landing.css`

### Agregar reglas responsive para elementos corporativos

**BUSCAR en `landing.css`:**

```css
@media (max-width: 480px) {
    .pilares-row { grid-template-columns: 1fr; }
    .badges-row { gap: 0.5rem; }
    .badge-cumpl { font-size: 0.75rem; padding: 0.4rem 0.8rem; }
    .hero-prueba-gratis { font-size: 0.82rem; }
}
```

**REEMPLAZAR por:**

```css
@media (max-width: 480px) {
    .pilares-row { grid-template-columns: 1fr; }
    .badges-row { gap: 0.5rem; }
    .badge-cumpl { font-size: 0.75rem; padding: 0.4rem 0.8rem; }
    .hero-prueba-gratis { font-size: 0.82rem; }
    .corp-hero-wordmark { font-size: 1.8rem; }
}
```

**BUSCAR en `landing.css`:**

```css
@media (max-width: 768px) {
    .hero { padding: 90px 0 64px; }
    .hero .tagline { font-size: 1.1rem; }
    .hero .subtitle { font-size: 1rem; }
    .hero .logo-hero { max-width: 240px; }
    .hero-screenshot { margin-top: 2rem; }
    section { padding: 56px 0; }
    section.section-compact { padding: 40px 0; }
    section.section-spacious { padding: 72px 0; }
    .section-title h2 { font-size: 1.5rem; }
    .section-title { margin-bottom: 2.5rem; }
    .contacto-info { padding-left: 0; margin-top: 1.5rem; }
    .precios-card { padding: 2rem 1.5rem; }
    .stat-item .num { font-size: 1.8rem; }
    .prueba-social-card { padding: 1.5rem; }
    .quien-detras {
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    .quien-texto .btn { align-self: center; }
    .pilares-row { grid-template-columns: 1fr 1fr; }
}
```

**REEMPLAZAR por (agregar 2 líneas al final del bloque):**

```css
@media (max-width: 768px) {
    .hero { padding: 90px 0 64px; }
    .hero .tagline { font-size: 1.1rem; }
    .hero .subtitle { font-size: 1rem; }
    .hero .logo-hero { max-width: 240px; }
    .hero-screenshot { margin-top: 2rem; }
    section { padding: 56px 0; }
    section.section-compact { padding: 40px 0; }
    section.section-spacious { padding: 72px 0; }
    .section-title h2 { font-size: 1.5rem; }
    .section-title { margin-bottom: 2.5rem; }
    .contacto-info { padding-left: 0; margin-top: 1.5rem; }
    .precios-card { padding: 2rem 1.5rem; }
    .stat-item .num { font-size: 1.8rem; }
    .prueba-social-card { padding: 1.5rem; }
    .quien-detras {
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    .quien-texto .btn { align-self: center; }
    .pilares-row { grid-template-columns: 1fr 1fr; }
    .corp-producto-card { padding: 2rem 1.25rem; }
    .corp-producto-logo { max-width: 200px; }
}
```

---

## Resumen de cambios

| # | Archivo | Qué cambia |
|---|---------|-----------|
| 1 | `templates/home.html` | Reescribe "Quiénes somos": historia de la empresa, sin leyes/SIFEN, con CTA |
| 2 | `templates/home.html` | Agrega CTA "Conocé Ñande ERP" al final de "Quiénes somos" |
| 3 | `templates/index.html` | Reescribe "¿Quién está detrás?": confianza personal, sin leyes/SIFEN |
| 4 | `templates/index.html` | Elimina `target="_blank"` de links a `/` (navbar + footer) |
| 5 | `templates/home.html` | Elimina `target="_blank"` de todos los links a `/nande-erp` |
| 6 | `templates/home.html` | Agrega WhatsApp flotante antes de `</body>` |
| 7 | `static/css/landing.css` | Agrega responsive para `.corp-hero-wordmark` en ≤480px |
| 8 | `static/css/landing.css` | Agrega responsive para `.corp-producto-card` y `.corp-producto-logo` en ≤768px |

## Después de aplicar los cambios

Correr el servidor local para verificar:

```bash
cd ~/landing-guaranisoft
source .venv/bin/activate
uvicorn main:app --reload
```

Abrir `http://localhost:8000/` y `http://localhost:8000/nande-erp` y verificar:
1. La sección "Quiénes somos" cuenta la historia de la empresa, no repite leyes/SIFEN
2. La sección "¿Quién está detrás?" habla personal, no repite leyes/SIFEN
3. Los links entre páginas no abren pestaña nueva
4. El WhatsApp flotante aparece en ambas páginas
5. En móvil (devtools 375px) el "GuaraníSoft" del hero no se ve desproporcionado
