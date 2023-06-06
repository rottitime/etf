import type { StoryObj, Meta } from '@storybook/html'
import { FieldMeta, Select, createMultiSelect, createSingleFieldWithMeta } from '../utils'

type Props = Select & FieldMeta

const list = [...Array(20).keys()].map((i) => `Option ${i}`)

const meta = {
  title: 'Components/Form/Multiselect',
  tags: ['autodocs'],
  render: ({ error, label, description, helperText, ...args }) =>
    createSingleFieldWithMeta(createMultiSelect(args), {
      error,
      label,
      description,
      helperText
    }),
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
    fullWidth: true,
    disabled: false
  }
}

export const Disabled: Story = {
  args: {
    ...Default.args,
    disabled: true
  }
}

export const Error: Story = {
  args: {
    ...Default.args,
    label: 'Type of problem',
    helperText: 'This is a invalid choice',
    description: 'A description helps users understand the context of the field',
    value: list[1],
    error: true
  }
}
