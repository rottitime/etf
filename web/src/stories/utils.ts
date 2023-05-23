import { FieldMeta, FormGroup, Input, Select, Textarea } from './types'

export const createInput = ({ fullWidth, dimension, onkeyup, ...props }: Input) => {
  const input = document.createElement('input')

  for (const [key, value] of Object.entries(props)) {
    input.setAttribute(key, value?.toString() || '')
  }
  fullWidth && input.classList.add('full-width')
  !!dimension && dimension !== 'medium' && input.classList.add(dimension)
  typeof onkeyup === 'function' && input.addEventListener('keyup', onkeyup)

  return input
}

const createHelperText = (text: string) => {
  const div = document.createElement('div')
  div.classList.add('helper')
  div.innerHTML = text
  return div
}

const createDescription = (text: string) => {
  const p = document.createElement('p')
  p.classList.add('description')
  p.innerHTML = text
  return p
}

const createLabel = (text: string, id: string) => {
  const label = document.createElement('label')
  label.setAttribute('for', id)
  label.innerHTML = text
  return label
}

export const createSelect = ({
  fullWidth,
  disabled,
  onchange,
  optionList,
  value,
  ...props
}: Select) => {
  const select = document.createElement('select')
  for (const [key, value] of Object.entries(props)) {
    select.setAttribute(key, value?.toString() || '')
  }
  select.innerHTML = `<option>Please select</option>`
  optionList.forEach((option) => {
    const optionElement = document.createElement('option')
    optionElement.value = option
    optionElement.text = option
    if (option === value) optionElement.setAttribute('selected', 'true')
    select.appendChild(optionElement)
  })
  fullWidth && select.classList.add('full-width')
  disabled && select.setAttribute('disabled', 'true')

  const wrapper = document.createElement('div')
  wrapper.classList.add('select')
  wrapper.appendChild(select)

  typeof onchange === 'function' && select.addEventListener('change', onchange)

  return wrapper
}

export const createTextarea = ({ fullWidth, onkeyup, ...props }: Textarea) => {
  const textarea = document.createElement('textarea')

  for (const [key, value] of Object.entries(props)) {
    textarea.setAttribute(key, value?.toString() || '')
  }
  fullWidth && textarea.classList.add('full-width')

  typeof onkeyup === 'function' && textarea.addEventListener('keyup', onkeyup)

  return textarea
}

export const createFormGroup = (
  elements: HTMLElement[] | HTMLElement,
  { error }: FormGroup
): HTMLDivElement => {
  const div = document.createElement('div')
  div.classList.add('form-group')
  error && div.classList.add('error')

  elements &&
    (elements instanceof Array
      ? elements.forEach((child) => div.appendChild(child))
      : div.appendChild(elements))

  return div
}

/* Combination of elements */
export const createSingleFieldWithMeta = (
  element: HTMLElement,
  { error, label, description, helperText }: FieldMeta
): HTMLElement => {
  if (label || helperText || description) {
    const formGroup = createFormGroup(element, { error, label, description, helperText })
    const id = crypto.randomUUID()
    description && formGroup.prepend(createDescription(description))
    label && formGroup.prepend(createLabel(label, id))
    helperText && formGroup.append(createHelperText(helperText))
    element.setAttribute('id', id)
    return formGroup
  }

  return element
}

export * from './types'
