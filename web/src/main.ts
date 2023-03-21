import './style/vars.css'
import './style/base.css'
import './style/template.css'
import './style/forms.css'
import './style/components.css'
import accordion from './components/accordion'
import icon from './components/icon'

//local development purposes only. to replace prod assets with dev
declare global {
  function myFunction(): boolean
  // eslint-disable-next-line no-var
  var devMode: boolean
}

if (import.meta.env.MODE === 'development') {
  globalThis.devMode = true
  ;['main-script', 'main-css'].forEach((id) => document.getElementById(id)?.remove())
}

window.addEventListener('load', () => {
  if (globalThis.devMode && import.meta.env.MODE === 'production') return
  accordion()
  icon()
})
