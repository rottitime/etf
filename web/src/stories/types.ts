export type Link = { href: string; text: string }

export type FieldMeta = {
  label?: string
  helperText?: string
  description?: string
  error?: boolean
}

export type Radio = {
  text: string
  large?: boolean
} & HTMLInputElement

export type Input = HTMLInputElement & {
  fullWidth: boolean
  dimension?: 'small' | 'medium' | 'large'
}

export type Textarea = HTMLTextAreaElement & {
  fullWidth: boolean
}

export type Select = {
  fullWidth: boolean
  list: string[]
} & HTMLSelectElement

export type Fieldset = {
  legend?: string
  elements: HTMLElement[] | HTMLElement
}

export type FormGroup = FieldMeta
