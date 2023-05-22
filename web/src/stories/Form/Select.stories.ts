import type { StoryObj, Meta } from '@storybook/html'
import { createSelect, Select as Props } from '../utils'

const meta = {
  title: 'Components/Form/Select',
  tags: ['autodocs'],
  render: createSelect,
  argTypes: {
    name: { control: 'text', table: { disable: true } },
    fullWidth: { control: 'boolean' },
    disabled: { control: 'boolean', defaultValue: false },
    onchange: { action: 'changed', table: { disable: true } }
  },
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=316-330&t=3c3246gboAwz7S3E-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const Default: Story = {
  args: {
    name: 'my-select',
    optionList: [...Array(5).keys()].map((i) => `Option ${i}`)
  }
}
