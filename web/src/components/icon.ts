class Govicon extends HTMLElement {
  constructor() {
    super()
    this.setup()
  }

  private async setup() {
    const iconName = this.getAttribute('key')
    const html = await import(`../svg/${iconName}.svg`)
    this.innerHTML = html.default
  }
}

const setupIcon = () => {
  customElements.define('gov-icon', Govicon)
}

export default setupIcon
