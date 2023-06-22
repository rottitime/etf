import {
  FieldMeta,
  FormGroup,
  Input,
  Select,
  Textarea,
  Radio,
  Checkbox,
  Icon,
  Button,
  Card
} from './types'

export const createCard = ({
  title,
  content,
  actions,
  onClick,
  accordion,
  open,
  small
}: Card) => {
  const card = document.createElement('div')
  card.classList.add('card')
  if (small) card.classList.add('small')

  //header
  const header = document.createElement('header')
  const h1 = document.createElement('h1')
  h1.textContent = title
  h1.classList.add('header2', 'highlight')
  header.append(h1)

  const p = document.createElement('p')
  p.textContent = content

  //accordion
  if (accordion) {
    card.classList.add('with-accordion')
    const content = document.createElement('div')
    content.classList.add('content')
    content.append(p)

    open
      ? header.setAttribute('aria-expanded', 'true')
      : header.setAttribute('aria-expanded', 'false')

    card.append(content)
  } else {
    card.append(p)
  }

  card.prepend(header)

  if (actions) {
    const footer = document.createElement('footer')
    footer.classList.add('actions')
    const btnPrimary = document.createElement('button')
    btnPrimary.classList.add('bttn-primary', 'primary-action')
    btnPrimary.setAttribute('type', 'submit')
    btnPrimary.textContent = 'Save'
    btnPrimary.addEventListener('click', onClick)

    const div = document.createElement('div')
    const btnCancel = document.createElement('a')
    btnCancel.classList.add('bttn-quaternary', 'small')
    btnCancel.setAttribute('href', '#')
    btnCancel.textContent = 'Cancel'
    btnCancel.addEventListener('click', onClick)

    // btnCancel.addEventListener('click', () => {
    //   action('Link Clicked')()
    // })

    const btnDelete = document.createElement('button')
    btnDelete.classList.add('bttn-negative', 'small')
    btnDelete.setAttribute('type', 'submit')
    btnDelete.textContent = 'Delete'
    btnDelete.addEventListener('click', onClick)
    div.append(btnCancel)
    div.append(btnDelete)
    footer.append(btnPrimary)
    footer.append(div)
    card.append(footer)
  }

  return card
}

export const createRadio = ({ text, large, ...props }: Radio): HTMLLabelElement => {
  const radio = document.createElement('input')
  radio.setAttribute('type', 'radio')
  for (const [key, value] of Object.entries(props)) {
    radio.setAttribute(key, value?.toString() || '')
  }

  const span = document.createElement('span')
  span.innerText = text

  const label = document.createElement('label')
  label.classList.add('radio')
  large && label.classList.add('large')
  label.append(radio, createCheckmark(), span)

  return label
}

export const createCheckbox = ({ text, large, ...props }: Checkbox): HTMLLabelElement => {
  const radio = document.createElement('input')
  radio.setAttribute('type', 'checkbox')
  for (const [key, value] of Object.entries(props)) {
    radio.setAttribute(key, value?.toString() || '')
  }

  const span = document.createElement('span')
  span.innerText = text

  const label = document.createElement('label')
  label.classList.add('checkbox')
  large && label.classList.add('large')
  label.append(radio, createCheckmark(), span)

  return label
}

export const createFieldset = (
  elements: HTMLElement[] | HTMLElement,
  legend?: string
): HTMLFieldSetElement => {
  const fieldset = document.createElement('fieldset')
  elements &&
    (elements instanceof Array
      ? elements.forEach((child) => fieldset.appendChild(child))
      : fieldset.appendChild(elements))

  if (legend) {
    const legendElement = document.createElement('legend')
    legendElement.innerText = legend
    fieldset.prepend(legendElement)
  }

  return fieldset
}

const createCheckmark = () => {
  const span = document.createElement('span')
  span.classList.add('checkmark')
  return span
}

export const createInput = ({
  fullWidth,
  dimension,
  className,
  onkeyup,
  ...props
}: Input) => {
  const input = document.createElement('input')

  for (const [key, value] of Object.entries(props)) {
    input.setAttribute(key, value?.toString() || '')
  }
  className && input.classList.add(className)
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
  list,
  value,
  ...props
}: Select) => {
  const select = document.createElement('select')
  for (const [key, value] of Object.entries(props)) {
    select.setAttribute(key, value?.toString() || '')
  }
  select.innerHTML = `<option value="">Please select</option>`
  list.forEach((option) => {
    const optionElement = document.createElement('option')
    optionElement.value = option
    optionElement.text = option
    if (option === value) optionElement.setAttribute('selected', 'true')
    select.appendChild(optionElement)
  })
  fullWidth && select.classList.add('full-width')
  disabled && select.setAttribute('disabled', 'true')

  const wrapper = document.createElement('div')
  wrapper.setAttribute('is', 'select-field')
  wrapper.appendChild(select)

  typeof onchange === 'function' && select.addEventListener('change', onchange)

  return wrapper
}

export const createMultiSelect = ({
  fullWidth,
  disabled,
  onchange,
  list,
  value,
  ...props
}: Select) => {
  const select = document.createElement('select')
  select.setAttribute('multiple', 'true')
  for (const [key, value] of Object.entries(props)) {
    select.setAttribute(key, value?.toString() || '')
  }

  list.forEach((option) => {
    const optionElement = document.createElement('option')
    optionElement.value = option
    optionElement.text = option
    if (option === value) optionElement.setAttribute('selected', '')
    select.appendChild(optionElement)
  })
  fullWidth && select.classList.add('full-width')
  disabled && select.setAttribute('disabled', 'true')

  const wrapper = document.createElement('div')
  wrapper.setAttribute('is', 'multi-select')
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

export const createButton = ({
  category = 'primary',
  small = false,
  label,
  onClick
}: Button) => {
  const btn = document.createElement('button')
  btn.type = 'button'
  btn.innerText = label
  if (onClick) {
    btn.addEventListener('click', onClick)
  }

  btn.className = [`bttn-${category}`, small ? 'small' : null].join(' ')

  return btn
}

export const createIcon = ({ key, size, color = '' }: Icon) => {
  const govIcon = document.createElement('gov-icon')
  govIcon.setAttribute('key', key)
  govIcon.style.fontSize = `${size}px`
  govIcon.style.color = color

  return govIcon
}

export * from './types'
