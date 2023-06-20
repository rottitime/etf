class Govicon extends HTMLElement {
  newCache?: Cache
  enableCache = true

  constructor() {
    super()
  }

  connectedCallback() {
    this.setup()
  }

  private async getIcon(icon: string) {
    if (this.enableCache) {
      const response = await this.newCache?.match(icon)
      if (response) return response.text()
    }
    const html = (await import(`../svg/${icon}.svg`)).default

    if (this.enableCache)
      this.newCache?.put(
        icon,
        new Response(html, { headers: { 'Content-Type': 'image/svg+xml' } })
      )

    return html
  }

  private async setup() {
    this.newCache = await caches.open('new-cache')
    const iconName = this.getAttribute('key')
    if (!iconName) return

    this.innerHTML = await this.getIcon(iconName)
  }
}

const setupIcon = () => {
  customElements.define('gov-icon', Govicon)
}

export default setupIcon
