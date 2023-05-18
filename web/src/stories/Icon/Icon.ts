// import icon from '../Icon/Icon'
import '../../main'

export interface Props {
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

/**
 * Primary UI component for user interaction
 */
export const createIcon = ({ key, size, color = '' }: Props) => {
  const govIcon = document.createElement('gov-icon')
  govIcon.setAttribute('key', key)
  govIcon.style.fontSize = `${size}px`
  govIcon.style.color = color

  return govIcon
}
