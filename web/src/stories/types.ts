export type Link = { href: string; text: string }

export type Input = HTMLInputElement & {
  fullWidth: boolean
  placeholder: string
  dimension?: 'small' | 'medium' | 'large'
}

export type Select = {
  fullWidth: boolean
  optionsList: string[]
} & HTMLSelectElement
