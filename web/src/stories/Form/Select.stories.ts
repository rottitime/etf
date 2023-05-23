import type { StoryObj, Meta } from '@storybook/html'
import { createSelect, createSingleFieldWithMeta, FieldMeta, Select } from '../utils'

type Props = Select & FieldMeta

const optionList = [...Array(5).keys()].map((i) => `Option ${i}`)

const meta = {
  title: 'Components/Form/Select',
  tags: ['autodocs'],
  render: ({ error, label, description, helperText, ...args }) =>
    createSingleFieldWithMeta(createSelect(args), {
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
    optionList
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
    value: optionList[1],
    error: true
  }
}
