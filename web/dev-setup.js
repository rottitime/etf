/* eslint-disable no-undef */
globalThis.devMode = true

//remove prod files so they don't conflict with dev scripts
window.addEventListener('load', () => {
  ;['main-script', 'main-css'].forEach((id) => document.getElementById(id)?.remove())
})
