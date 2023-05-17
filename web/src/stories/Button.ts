// import './button.css'
import '../style/vars.css'
import '../style/base.css'
import '../style/components/buttons.css'

export interface ButtonProps {
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

/**
 * Primary UI component for user interaction
 */
export const createButton = ({
  category = 'primary',
  small = false,
  label,
  onClick
}: ButtonProps) => {
  const btn = document.createElement('button')
  btn.type = 'button'
  btn.innerText = label
  if (onClick) {
    btn.addEventListener('click', onClick)
  }

  btn.className = [`bttn-${category}`, small ? 'small' : null].join(' ')

  return btn
}
