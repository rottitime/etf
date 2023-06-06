import type { StoryObj, Meta } from '@storybook/html'
import { FieldMeta, Select } from '../utils'

type Props = Select & FieldMeta

const list = [...Array(20).keys()].map((i) => `Option ${i}`)

const meta = {
  title: 'Components/Form/Multiselect',
  tags: ['autodocs'],
  render: ({ error, label, description, helperText, ...args }) =>
    `<div is='multi-select'>
    <select multiple name="demo" class="full-width">
    ${list.map((option) => `<option>${option}</option>`).join('')}
    </select>
    </div>`,
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
    list
  }
}

export const Labels: Story = {
  args: {
    ...Default.args,
    label: 'Type of problem',
    helperText: 'This is a invalid choice',
    description: 'A description helps users understand the context of the field',
    fullWidth: true
  }
}

export const Error: Story = {
  args: {
    ...Labels.args,
    value: list[1],
    error: true
  }
}
