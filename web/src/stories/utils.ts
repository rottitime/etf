import { Input } from './types'

export const createInput = ({ fullWidth, onkeyup, ...props }: Input) => {
  const input = document.createElement('input')

  for (const [key, value] of Object.entries(props)) {
    input.setAttribute(key, value?.toString() || '')
  }
  fullWidth && input.classList.add('full-width')
  !!onkeyup && typeof onkeyup === 'function' && input.addEventListener('keyup', onkeyup)

  return input
}

export * from './types'
