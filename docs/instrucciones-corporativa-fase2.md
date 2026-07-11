# Instrucciones para Claude Code — Enriquecer página corporativa GuaraníSoft

> Proyecto: `\\wsl.localhost\Ubuntu-24.04\home\victor\landing-guaranisoft`
> Archivo a editar: `templates/home.html` (todos los cambios en este archivo)
> Objetivo: pasar de 4 secciones minimalistas a 7 secciones que vendan la empresa como entidad confiable.

---

## Cambio 1 — Agregar sección "Por qué GuaraníSoft" (entre "Quiénes somos" y "Nuestro producto")

**BUSCAR en `templates/home.html`:**

```html
<!-- ═══ Nuestro producto ═══════════════════════════════════════════════ -->
<section id="producto" aria-labelledby="producto-heading">
```

**INSERTAR ANTES de esa línea:**

```html
<!-- ═══ Por qué GuaraníSoft ═════════════════════════════════════════════ -->
<section class="pilares section-compact" id="por-que" aria-labelledby="por-que-heading">
    <div class="container">
        <div class="section-title fade-in">
            <h2 id="por-que-heading">Por qué GuaraníSoft</h2>
            <p>Cuatro razones que nos diferencian como empresa</p>
        </div>
        <div class="pilares-row stagger-children">
            <div class="pilar fade-in">
                <div class="pilar-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 2 L2 7 L12 12 L22 7 Z"/><path d="M2 17 L12 22 L22 17"/><path d="M2 12 L12 17 L22 12"/></svg>
                </div>
                <h4>Hecho en Paraguay</h4>
                <p>No adaptamos software extranjero. Lo construimos desde cero para la realidad fiscal y comercial local.</p>
            </div>
            <div class="pilar fade-in">
                <div class="pilar-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                </div>
                <h4>Una década de software local</h4>
                <p>Más de 10 años escribiendo código para empresas paraguayas. No es un experimento, es trayectoria.</p>
            </div>
            <div class="pilar fade-in">
                <div class="pilar-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 9 L12 2 L21 9 L21 22 L3 22 Z"/><line x1="9" y1="22" x2="9" y2="12"/><line x1="15" y1="22" x2="15" y2="12"/></svg>
                </div>
                <h4>PyMEs primero</h4>
                <p>Diseñamos para el comerciante que atiende en el mostrador, no para corporativos con departamento de IT.</p>
            </div>
            <div class="pilar fade-in">
                <div class="pilar-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21 11.5 C21 16 17 19 12 19 C10.5 19 9 18.7 7.7 18.2 L3 19 L4.3 15.5 C3.5 14.4 3 13 3 11.5 C3 7 7 4 12 4 C17 4 21 7 21 11.5 Z"/></svg>
                </div>
                <h4>Soporte sin intermediarios</h4>
                <p>Cuando escribís, te responde quien programa. Sin call center, sin tickets, sin vueltas.</p>
            </div>
        </div>
    </div>
</section>

```

---

## Cambio 2 — Agregar sección de stats corporativos (después de "Por qué GuaraníSoft", antes de "Nuestro producto")

**BUSCAR en `templates/home.html` (justo después del cierre de la sección anterior que acabas de agregar):**

```html
<!-- ═══ Nuestro producto ═══════════════════════════════════════════════ -->
<section id="producto" aria-labelledby="producto-heading">
```

**INSERTAR ANTES de esa línea:**

```html
<!-- ═══ Stats corporativos ═════════════════════════════════════════════ -->
<section class="stats section-compact" aria-label="Indicadores de la empresa">
    <div class="container">
        <div class="row g-4 stagger-children">
            <div class="col-6 col-md-3 fade-in">
                <div class="stat-item">
                    <span class="num">10+ años</span>
                    <span class="label">Escribiendo software para empresas paraguayas.</span>
                </div>
            </div>
            <div class="col-6 col-md-3 fade-in">
                <div class="stat-item">
                    <span class="num">100% local</span>
                    <span class="label">Desarrollo paraguayo, sin outsourcing.</span>
                </div>
            </div>
            <div class="col-6 col-md-3 fade-in">
                <div class="stat-item">
                    <span class="num">1 producto</span>
                    <span class="label">Enfocados en hacer una cosa y hacerla bien.</span>
                </div>
            </div>
            <div class="col-6 col-md-3 fade-in">
                <div class="stat-item">
                    <span class="num">0 call centers</span>
                    <span class="label">Soporte directo de quien programa.</span>
                </div>
            </div>
        </div>
    </div>
</section>

```

---

## Cambio 3 — Acortar descripción de Ñande ERP en "Nuestro producto"

**BUSCAR en `templates/home.html`:**

```html
            <p class="corp-producto-desc">
                Punto de Venta, Inventario, Cajas y Contabilidad conectados en un solo
                sistema. Diseñado para PyMEs paraguayas: cumplimiento Ley 6380 y SIFEN,
                funciona sin internet y con soporte local directo.
            </p>
```

**REEMPLAZAR por:**

```html
            <p class="corp-producto-desc">
                El sistema de gestión integral que ordena tu empresa. Pensado para PyMEs paraguayas, con cumplimiento fiscal local y soporte directo.
            </p>
```

**Por qué:** La descripción actual duplica el hero de la página de producto. Una frase corta + CTA es suficiente; los detalles están en `/nande-erp`.

---

## Cambio 4 — Retirar `soporte@guaranisof.com` de la sección Contacto

**BUSCAR en `templates/home.html`:**

```html
                        <li>
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>
                            <a href="mailto:soporte@guaranisof.com">soporte@guaranisof.com</a>
                        </li>
```

**REEMPLAZAR por:**

```html
                        <li>
                            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51l-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347"/></svg>
                            <a href="https://wa.me/595992504620" target="_blank" rel="noopener">+595 992 504 620</a>
                        </li>
```

**Por qué:** `soporte@` es un canal de producto (clientes que ya usan el sistema). En la corporativa, el WhatsApp es más útil como punto de contacto. Esto reemplaza el email de soporte por el teléfono/WhatsApp, que ya no estaba en la lista de contacto de la corporativa.

> ⚠️ **Nota:** Si el WhatsApp ya aparece más abajo en la lista, eliminar este bloque entero en lugar de reemplazarlo. Verificar que no queden duplicados.

---

## Cambio 5 — Agregar formulario de contacto en la sección Contacto

**BUSCAR en `templates/home.html` (la sección de contacto actual):**

```html
        <div class="row justify-content-center">
            <div class="col-lg-5 fade-in">
                <div class="contacto-info">
```

**REEMPLAZAR por (agregar columna de formulario antes de la info):**

```html
        <div class="row justify-content-center">
            <div class="col-lg-7 fade-in">
                <div class="contacto-form">
                    <form id="formContactoCorp" onsubmit="return false;" aria-label="Formulario de contacto corporativo">
                        <div class="row g-3">
                            <div class="col-md-6">
                                <label class="form-label" for="corp-nombre">Nombre *</label>
                                <input type="text" name="nombre" id="corp-nombre" class="form-control" required aria-required="true">
                            </div>
                            <div class="col-md-6">
                                <label class="form-label" for="corp-email">Email *</label>
                                <input type="email" name="email" id="corp-email" class="form-control" required aria-required="true">
                            </div>
                            <div class="col-12">
                                <label class="form-label" for="corp-mensaje">¿En qué te podemos ayudar? *</label>
                                <textarea name="mensaje" id="corp-mensaje" class="form-control" rows="4" required aria-required="true"></textarea>
                            </div>
                            <div class="col-12">
                                <button type="submit" class="btn btn-morado w-100" id="btnContactoCorp">
                                    <span id="corpBtnText">
                                        <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 0.5rem; vertical-align: -3px;"><path d="M22 2 L11 13"/><path d="M22 2 L15 22 L11 13 L2 9 Z"/></svg>
                                        Enviar consulta
                                    </span>
                                    <span id="corpBtnSpinner" class="d-none">
                                        <span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>Enviando...
                                    </span>
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
            <div class="col-lg-5 fade-in">
                <div class="contacto-info">
```

**Por qué:** La corporativa necesita su propio formulario. 3 campos simples (Nombre, Email, Consulta) sin orientación a demo. Usa el mismo endpoint `POST /contacto` del backend.

---

## Cambio 6 — Agregar JavaScript del formulario (antes del cierre de `</body>`)

**BUSCAR en `templates/home.html`:**

```html
// ── Fade-in ──
var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(e) {
        if (e.isIntersecting) e.target.classList.add('visible');
    });
}, { threshold: 0.1 });

document.querySelectorAll('.fade-in').forEach(function(el) { observer.observe(el); });
```

**INSERTAR DESPUÉS de esa línea (antes de `</script>`):**

```javascript

// ── Toast container ──
(function() {
    var container = document.createElement('div');
    container.id = 'toast-container';
    document.body.appendChild(container);
})();

function showToast(type, message) {
    var container = document.getElementById('toast-container');
    var toast = document.createElement('div');
    var bgColor = type === 'success' ? '#D1FAE5' : '#FEF3C7';
    var borderColor = type === 'success' ? '#6EE7B7' : '#FCD34D';
    var textColor = type === 'success' ? '#065F46' : '#92400E';
    toast.style.cssText = 'background:' + bgColor + ';border:1px solid ' + borderColor + ';color:' + textColor + ';border-radius:10px;padding:0.9rem 1.1rem;display:flex;align-items:flex-start;gap:0.5rem;box-shadow:0 8px 24px rgba(0,0,0,0.12);opacity:0;transform:translateX(24px);transition:opacity 0.25s ease,transform 0.25s ease;font-size:0.88rem;line-height:1.4;';
    toast.innerHTML = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-top:2px;flex-shrink:0;"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>' + message + '</span>';
    container.appendChild(toast);
    requestAnimationFrame(function() {
        toast.style.opacity = '1';
        toast.style.transform = 'translateX(0)';
    });
    setTimeout(function() {
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(24px)';
        setTimeout(function() { toast.remove(); }, 250);
    }, 6000);
}

// ── Formulario corporativo AJAX ──
document.getElementById('formContactoCorp').addEventListener('submit', function(e) {
    e.preventDefault();
    var btn = document.getElementById('btnContactoCorp');
    if (btn.disabled) return;
    btn.disabled = true;
    document.getElementById('corpBtnText').classList.add('d-none');
    document.getElementById('corpBtnSpinner').classList.remove('d-none');

    var formData = new FormData(this);

    fetch('/contacto', { method: 'POST', body: formData })
        .then(function(r) {
            if (r.status === 429) {
                document.getElementById('corpBtnSpinner').classList.add('d-none');
                document.getElementById('corpBtnText').classList.remove('d-none');
                btn.disabled = false;
                showToast('warning', 'Ya enviaste un mensaje. Por favor esperá 60 segundos antes de intentar de nuevo.');
                return null;
            }
            if (!r.ok) throw new Error('HTTP ' + r.status);
            return r.json();
        })
        .then(function(data) {
            if (!data) return;
            document.getElementById('corpBtnSpinner').classList.add('d-none');
            document.getElementById('corpBtnText').classList.remove('d-none');
            btn.disabled = false;
            document.getElementById('formContactoCorp').reset();
            showToast('success', '¡Recibimos tu consulta! Te respondemos pronto.');
        })
        .catch(function(err) {
            document.getElementById('corpBtnSpinner').classList.add('d-none');
            document.getElementById('corpBtnText').classList.remove('d-none');
            btn.disabled = false;
            showToast('warning', 'Ocurrió un error al enviar. Probá de nuevo o escribinos directo por WhatsApp.');
        });
});
```

---

## Resumen de cambios

| # | Qué | Sección |
|---|-----|---------|
| 1 | Nueva sección "Por qué GuaraníSoft" con 4 pilares corporativos | Nueva |
| 2 | Nueva sección de stats corporativos (10+ años, 100% local, 1 producto, 0 call centers) | Nueva |
| 3 | Acortar descripción de Ñande ERP a una frase + CTA | "Nuestro producto" |
| 4 | Reemplazar `soporte@` por WhatsApp en datos de contacto | "Contacto" |
| 5 | Agregar formulario de 3 campos (Nombre, Email, Consulta) | "Contacto" |
| 6 | Agregar JS del formulario (AJAX + toast + rate limiting) | `<script>` |

## Después de aplicar

```bash
cd ~/landing-guaranisoft
source .venv/bin/activate
uvicorn main:app --reload
```

Verificar en `http://localhost:8000/`:
1. La página tiene 7 secciones: Hero → Quiénes somos → Por qué GuaraníSoft → Stats → Nuestro producto → Contacto (con formulario) → Footer
2. Los pilares corporativos se ven como los del producto (mismo diseño, distinto contenido)
3. Los stats corporativos tienen fondo morado como los del producto
4. El formulario envía correctamente (probar con datos de prueba)
5. El toast de éxito aparece al enviar
6. En móvil (375px) todo se ve bien
