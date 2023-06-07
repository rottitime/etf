class MultiSelect extends HTMLDivElement {
  multiValues: string[] = []

  constructor() {
    super()
  }

  connectedCallback() {
    this.setup()
  }

  private createTag(value: string) {
    const tag = document.createElement('div')
    tag.classList.add('chip')
    tag.innerHTML = value

    const icon = document.createElement('gov-icon')
    icon.classList.add('close')
    icon.setAttribute('key', 'cross')
    icon.setAttribute('role', 'button')
    icon.addEventListener('click', () => this.multiRemove(value), true)
    tag.appendChild(icon)
    return tag
  }

  private createMuliSelect() {
    const multiselect = document.createElement('selectmenu')
    const source = this.querySelector('select')
    //copy all attributes from multiselect
    Array.from(source?.attributes || []).forEach((attribute) => {
      multiselect.setAttribute(
        attribute.nodeName === 'id' ? 'data-id' : attribute.nodeName,
        attribute?.nodeValue || ''
      )
    })
    const options = source?.querySelectorAll<HTMLOptionElement>('option') || []

    const button = document.createElement('div')

    button.setAttribute('slot', 'button')
    button.setAttribute('behavior', 'button')
    multiselect.prepend(button)

    options.forEach((option) => {
      if (option.selected) this.multiAdd(option.value)
      multiselect.appendChild(option.cloneNode(true))
    })

    //seelected value element
    const selectedValue = document.createElement('div')
    selectedValue.setAttribute('slot', 'selected-value')
    selectedValue.setAttribute('behavior', 'selected-value')
    multiselect.appendChild(selectedValue)

    multiselect.addEventListener('click', (e) => {
      const option = (e.target as HTMLElement)?.closest('option')
      if (!option) return

      const newValue: string = option.value
      this.multiValues.includes(newValue)
        ? this.multiRemove(newValue)
        : this.multiAdd(newValue)
    })

    return multiselect
  }

  private multiAdd(value: string) {
    this.multiValues.push(value)
    this.multiRefreshSelectedValues()
    this.multiRefreshOptions()
  }

  private multiRemove(toRemove: string) {
    this.multiValues = this.multiValues.filter((value) => value !== toRemove)

    this.multiRefreshSelectedValues()
    this.multiRefreshOptions()
  }

  private multiRefreshSelectedValues() {
    const selectedValues = this.querySelector('.selected-values')
    if (selectedValues) {
      selectedValues.innerHTML = ''
      this.multiValues.forEach((value) =>
        selectedValues.appendChild(this.createTag(value))
      )
    }
  }

  private multiRefreshOptions() {
    const multiselect = this.querySelector('selectmenu') as HTMLSelectElement
    const options = (multiselect && multiselect.querySelectorAll('option')) || []
    const optionsHidden = this.querySelector('select')?.querySelectorAll('option') || []
    options.forEach((option, index) => {
      if (this.multiValues.includes(option.value)) {
        option.setAttribute('selected', '')
        optionsHidden[index].setAttribute('selected', '')
      } else {
        option.removeAttribute('selected')
        optionsHidden[index].removeAttribute('selected')
      }
    })
  }

  private setup() {
    const selectedValues = document.createElement('div')
    selectedValues.classList.add('selected-values')
    this.prepend(this.createMuliSelect())
    this.prepend(selectedValues)

    // this.querySelector('select')?.replaceWith(this.createMuliSelect())

    this.multiRefreshSelectedValues()
    this.multiRefreshOptions()
  }
}

const setupMultiselect = () =>
  customElements.define('multi-select', MultiSelect, { extends: 'div' })

export default setupMultiselect
