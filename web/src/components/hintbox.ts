class HintBox extends HTMLElement {
  constructor() {
    super()
  }

  connectedCallback() {
    this.setAttribute('hidden', 'true') //hide while rendering. prevents flash of unstyled content
    setTimeout(() => this.setup())
  }

  private setup() {
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
    toggleBtn.innerHTML =
      '<gov-icon key="help"></gov-icon>' + (this.getAttribute('aria-label') || 'Hint')
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
    this.removeAttribute('hidden')
  }
}

const setupHintbox = () => customElements.define('hint-box', HintBox)

export default setupHintbox
