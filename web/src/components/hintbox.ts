import help from '../svg/help.svg'

class Hintbox extends HTMLDivElement {
  constructor() {
    super()
    this.setupDom()
  }

  private setupDom() {
    const id = crypto.randomUUID()
    const idContent = `content_${id}`
    const idButton = `button_${id}`
    const content = this.querySelector('.content')
    if (!content) return

    //button setup
    const toggleBtn = document.createElement('button')
    toggleBtn.setAttribute('id', idButton)
    toggleBtn.classList.add('txt-link')
    toggleBtn.setAttribute('type', 'button')
    toggleBtn.setAttribute('aria-expanded', this.dataset.open || 'false')
    toggleBtn.setAttribute('aria-controls', idContent)
    toggleBtn.innerHTML = help + (this.getAttribute('aria-label') || 'Hint')
    toggleBtn.addEventListener('click', () => {
      const opened = toggleBtn.getAttribute('aria-expanded') === 'true'
      toggleBtn.setAttribute('aria-expanded', String(!opened))
    })
    this.prepend(toggleBtn)

    //content wrapper
    const wrapper = document.createElement('div')
    const parent = content.parentNode
    wrapper.classList.add('content-wrapper')
    wrapper.setAttribute('id', idContent)
    wrapper.setAttribute('aria-labelledby', idButton)
    wrapper.setAttribute('role', 'region')
    parent?.insertBefore(wrapper, content)
    wrapper.appendChild(content)
  }
}

const setupHintbox = () => {
  customElements.define('hint-box', Hintbox, { extends: 'div' })
}

export default setupHintbox
