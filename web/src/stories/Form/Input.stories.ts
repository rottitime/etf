import type { StoryObj, Meta } from '@storybook/html'

type Props = HTMLInputElement & {
  fullWidth: boolean
  placeholder: string
}

export const createInput = ({ fullWidth, ...props }: Props) => {
  const input = document.createElement('input')

  for (const [key, value] of Object.entries(props)) {
    input.setAttribute(key, value?.toString() || '')
  }
  fullWidth && input.classList.add('full-width')
  return input
}

/**
 * Standard input field
 */
const meta = {
  title: 'Components/Form/Input',
  tags: ['autodocs'],
  render: createInput,
  argTypes: {
    fullWidth: { control: 'boolean' },
    value: { control: 'text' },
    placeholder: { control: 'text' }
  },
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=27-75&t=ur05zeF7bSVeJzta-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const Default: Story = {
  args: {
    placeholder: 'e.g. Joe Blogs',
    type: 'text'
  }
}
