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

export type Checkbox = {
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

export interface Button {
  category: 'primary' | 'secondary' | 'tertiary' | 'negative'

  small?: boolean
  /**
   * Button contents
   */
  label: string
  /**
   * Optional click handler
   */
  onClick?: () => void
}

export interface Icon {
  key:
    | 'add'
    | 'arrow-down'
    | 'arrow-up'
    | 'calendar'
    | 'chevron-down'
    | 'crest'
    | 'cross'
    | 'error'
    | 'help'
    | 'logo'
    | 'menu'
    | 'new-tab'
    | 'pencil'
    | 'search'
    | 'success'
    | 'tick'
    | 'warning'
  color?: string
  size?: number
}
