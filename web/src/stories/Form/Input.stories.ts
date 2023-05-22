import type { StoryObj, Meta } from '@storybook/html'
import { createInput, Input as Props } from '../utils'

/**
 * Standard input field
 */
const meta = {
  title: 'Components/Form/Input',
  tags: ['autodocs'],
  render: createInput,
  argTypes: {
    fullWidth: { control: 'boolean' },
    onkeyup: { action: 'changed', table: { disable: true } },
    dimension: {
      control: { type: 'select' },
      options: ['small', 'medium', 'large']
    }
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
    dimension: 'medium',
    type: 'text'
  }
}
