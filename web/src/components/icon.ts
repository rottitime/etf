class Govicon extends HTMLElement {
  constructor() {
    super()
  }

  connectedCallback() {
    this.setup()
  }

  private async setup() {
    const iconName = this.getAttribute('key')
    if (!iconName) return
    const html = await import(`../svg/${iconName}.svg`)
    this.innerHTML = html.default
  }
}

const setupIcon = () => {
  customElements.define('gov-icon', Govicon)
}

export default setupIcon
