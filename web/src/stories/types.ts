export type Link = { href: string; text: string }

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
