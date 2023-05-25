import type { StoryObj, Meta } from '@storybook/html'
import { createTextarea, Textarea, createSingleFieldWithMeta, FieldMeta } from '../utils'

type Props = Textarea & FieldMeta

const meta = {
  title: 'Components/Form/Textarea',
  tags: ['autodocs'],
  render: ({ error, label, description, helperText, ...args }) =>
    createSingleFieldWithMeta(createTextarea(args), {
      error,
      label,
      description,
      helperText
    }),
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
    label: 'Short descritpion',
    placeholder: 'e.g. Describe your problem here'
  }
}

export const Description: Story = {
  args: {
    ...Default.args,
    helperText: 'Only user letters and not numbers',
    description: 'A description helps users understand the context of the field'
  }
}

export const Error: Story = {
  args: {
    ...Description.args,
    error: true
  }
}
