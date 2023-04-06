const setButtonState = (open: boolean) => {
  open
    ? document.querySelector('body')?.classList.add('darken')
    : document.querySelector('body')?.classList.remove('darken')
  ;(document.getElementById('main-header-mobile-menu') as HTMLButtonElement).setAttribute(
    'aria-expanded',
    Boolean(open).toString()
  )
}

export const cleanup = () => setButtonState(false)

const setupMobileMenu = () => {
  document
    .getElementById('main-header-mobile-menu')
    ?.addEventListener('click', (e) =>
      setButtonState(
        (e.currentTarget as HTMLButtonElement).getAttribute('aria-expanded') !== 'true'
      )
    )
}

export default setupMobileMenu
