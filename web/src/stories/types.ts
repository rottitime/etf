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
}

export type Textarea = HTMLTextAreaElement & {
  fullWidth: boolean
}

export type Select = {
  fullWidth: boolean
  optionList: string[]
} & HTMLSelectElement

export type FormGroup = FieldMeta
