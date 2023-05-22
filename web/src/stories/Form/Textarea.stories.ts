import type { StoryObj, Meta } from '@storybook/html'
import { createTextarea, Textarea as Props } from '../utils'

const meta = {
  title: 'Components/Form/Textarea',
  tags: ['autodocs'],
  render: createTextarea,
  argTypes: {
    fullWidth: { control: 'boolean' },
    placeholder: { control: 'text' },
    onkeyup: { action: 'changed', table: { disable: true } }
  },
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=481-954&t=suZkdl8uVnyH6HpY-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const Default: Story = {
  args: {
    placeholder: 'e.g. Joe Blogs'
  }
}
