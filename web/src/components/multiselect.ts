type MultiValue = {
  value: string
  text: string
}

class MultiSelect extends HTMLDivElement {
  multiValues: MultiValue[] = []

  constructor() {
    super()
  }

  connectedCallback() {
    setTimeout(() => this.setup())
  }

  private createTag(option: MultiValue) {
    const tag = document.createElement('div')
    tag.classList.add('chip')
    tag.innerHTML = option.text

    const icon = document.createElement('gov-icon')
    icon.classList.add('close')
    icon.setAttribute('key', 'cross')
    icon.setAttribute('role', 'button')
    icon.addEventListener('click', () => this.multiRemove(option), true)
    tag.appendChild(icon)
    return tag
  }

  private createMuliSelect() {
    // Create a <selectmenu> element to replace the original <select> element
    const multiselect = document.createElement('selectmenu')
    // Copy data-* attributes from the <select> element to the <selectmenu> element
    const source = this.querySelector('select')

    Array.from(source?.attributes || []).forEach((attribute) => {
      multiselect.setAttribute(
        attribute.nodeName === 'id' ? 'data-id' : attribute.nodeName,
        attribute?.nodeValue || ''
      )
    })
    // Copy <option> elements from the <select> element to the <selectmenu> element
    const options = source?.querySelectorAll<HTMLOptionElement>('option') || []

    const button = document.createElement('div')

    button.setAttribute('slot', 'button')
    button.setAttribute('behavior', 'button')
    multiselect.prepend(button)

    options.forEach((option) => {
      if (option.selected) this.multiAdd({ value: option.value, text: option.innerText })
      multiselect.appendChild(option.cloneNode(true))
    })

    const selectedValue = document.createElement('div')
    selectedValue.setAttribute('slot', 'selected-value')
    selectedValue.setAttribute('behavior', 'selected-value')
    multiselect.appendChild(selectedValue)

    multiselect.addEventListener('click', (e) => {
      const option = (e.target as HTMLOptionElement)?.closest('option')
      if (!option) return

      const newValue = { value: option.value, text: option.text }

      this.multiValues.find(({ value }) => value === newValue.value)
        ? this.multiRemove(newValue)
        : this.multiAdd(newValue)
    })

    return multiselect
  }

  private multiAdd(value: MultiValue) {
    this.multiValues.push(value)
    this.multiRefreshSelectedValues()
    this.multiRefreshOptions()
  }

  private multiRemove(toRemove: MultiValue) {
    this.multiValues = this.multiValues.filter(({ value }) => value !== toRemove.value)

    this.multiRefreshSelectedValues()
    this.multiRefreshOptions()
  }

  private multiRefreshSelectedValues() {
    // Get the container element for the selected values
    const selectedValues = this.querySelector('.selected-values')
    // If it exists, clear it
    if (selectedValues) {
      selectedValues.innerHTML = ''
      // For each selected value, create a tag and append it to the container
      this.multiValues.forEach((option) =>
        selectedValues.appendChild(this.createTag(option))
      )
    }
  }

  private multiRefreshOptions() {
    const multiselect = this.querySelector('selectmenu') as HTMLSelectElement
    const options = (multiselect && multiselect.querySelectorAll('option')) || []
    const optionsHidden = this.querySelector('select')?.querySelectorAll('option') || []
    options.forEach((option, index) => {
      if (this.multiValues.find(({ value }) => value === option.value)) {
        option.setAttribute('selected', '')
        optionsHidden[index].setAttribute('selected', '')
      } else {
        option.removeAttribute('selected')
        optionsHidden[index].removeAttribute('selected')
      }
    })
  }

  // Create a div to store the selected values
  private setup() {
    const selectedValues = document.createElement('div')
    selectedValues.classList.add('selected-values')

    // Hide the original select element and prepend the new elements
    this.querySelector('select')?.setAttribute('hidden', '')
    this.prepend(this.createMuliSelect())
    this.prepend(selectedValues)

    // Add the selected values and options to the new elements
    this.multiRefreshSelectedValues()
    this.multiRefreshOptions()
  }
}

const setupMultiselect = () =>
  customElements.define('multi-select', MultiSelect, { extends: 'div' })

export default setupMultiselect
