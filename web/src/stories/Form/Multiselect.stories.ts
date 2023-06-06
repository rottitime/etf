import type { StoryObj, Meta } from '@storybook/html'
import { FieldMeta, Select } from '../utils'

type Props = Select & FieldMeta

const list = [...Array(20).keys()].map((i) => `Option ${i}`)

const meta = {
  title: 'Components/Form/Multiselect',
  tags: ['autodocs'],
  render: ({ name, fullWidth, list, disabled }) =>
    `<div is='multi-select'>
    <select multiple name="${name}" class="${fullWidth ? 'full-width' : ''}" ${
      disabled ? 'disabled' : ''
    }>
    ${list.map((option) => `<option>${option}</option>`).join('')}
    </select>
    </div>

    `,
  argTypes: {
    name: { control: 'text', table: { disable: true } },
    fullWidth: { control: 'boolean' },
    disabled: { control: 'boolean', defaultValue: false },
    onchange: { action: 'changed', table: { disable: true } }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const Default: Story = {
  args: {
    name: 'my-select',
    list,
    fullWidth: false,
    disabled: false
  }
}

export const Disabled: Story = {
  args: {
    ...Default.args,
    disabled: true
  }
}
