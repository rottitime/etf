const showAllText = ['Show all sections', 'Hide all sections']

class Accordion extends HTMLDivElement {
  buttonId: string
  sectionId: string

  constructor() {
    super()

    const id = crypto.randomUUID()
    this.buttonId = `btn-${id}`
    this.sectionId = `pnl-${id}`
  }

  connectedCallback() {
    setTimeout(() => this.setup())
  }

  private setupPanels() {
    this.querySelectorAll('.accordion-panel').forEach((panel, i) => {
      panel.setAttribute('role', 'region')
      panel.setAttribute('aria-labelledby', this.buttonId + `-${i}`)
      panel.id = this.sectionId + `-${i}`
    })
  }

  private isAllOpen = () =>
    this.querySelectorAll('.accordion-title[aria-expanded="false"]').length === 0

  private setupButtons() {
    this.querySelectorAll('.accordion-title').forEach((button, i) => {
      button.setAttribute('role', 'button')
      button.id = this.buttonId + `-${i}`
      button.setAttribute(
        'aria-expanded',
        String(button.getAttribute('aria-expanded') === 'true' || false)
      )
      button.setAttribute('aria-controls', this.sectionId + `-${i}`)

      //event to toggle aria-expanded
      button.addEventListener('click', () => {
        button.setAttribute(
          'aria-expanded',
          String(!(button.getAttribute('aria-expanded') === 'true' || false))
        )
        this.isAllOpen() && this.setShowAllState(true)
      })
    })
  }

  private setShowAllState(open: boolean) {
    const showAll = this.querySelector<HTMLButtonElement>('.show-all')
    if (showAll) {
      showAll.setAttribute('aria-expanded', String(open))
      showAll.innerText = open ? showAllText[1] : showAllText[0]
    }
  }

  private createShowAll() {
    const button = document.createElement('button')
    button.setAttribute('type', 'button')
    button.setAttribute('class', 'show-all')
    button.setAttribute('aria-expanded', 'false')
    button.innerText = showAllText[0]

    button.addEventListener('click', () => {
      const expanded = button.getAttribute('aria-expanded') === 'true' || false

      this.setShowAllState(!expanded)

      this.querySelectorAll('.accordion-title').forEach((btn) =>
        btn.setAttribute('aria-expanded', String(!expanded))
      )
    })
    return button
  }

  private setup() {
    this.setupButtons()
    this.setupPanels()
    const showAll = this.createShowAll()

    this.prepend(showAll)
  }
}

const setupAccordion = () =>
  customElements.define('idotai-accordion', Accordion, { extends: 'div' })

export default setupAccordion
