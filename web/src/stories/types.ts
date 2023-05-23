export type Link = { href: string; text: string }

export type FieldMeta = {
  label?: string
  helperText?: string
  description?: string
  error?: boolean
}

export type Input = HTMLInputElement & {
  fullWidth: boolean
  dimension?: 'small' | 'medium' | 'large'
} & FieldMeta

export type Textarea = HTMLTextAreaElement & {
  fullWidth: boolean
}

export type Select = {
  fullWidth: boolean
  optionList: string[]
} & HTMLSelectElement

export type FormGroup = {
  elements: HTMLElement[] | HTMLElement
  error?: boolean
} & FieldMeta
