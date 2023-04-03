const setupMobileMenu = () => {
  document.getElementById('main-header-mobile-menu2')?.addEventListener('click', (e) => {
    const button = e.currentTarget as HTMLButtonElement
    const isOpen = button.getAttribute('aria-expanded') === 'true'

    if (isOpen) {
      document.querySelector('body')?.classList.remove('darken')
      button.setAttribute('aria-expanded', Boolean(!isOpen).toString())
    } else {
      document.querySelector('body')?.classList.add('darken')
      button.setAttribute('aria-expanded', Boolean(!isOpen).toString())
    }
  })
}

export default setupMobileMenu
