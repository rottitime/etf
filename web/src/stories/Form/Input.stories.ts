import type { StoryObj, Meta } from '@storybook/html'
import { createInput, createSingleFieldWithMeta, FieldMeta, Input } from '../utils'

type Props = Input & FieldMeta

/**
 * Standard input field
 */
const meta = {
  title: 'Components/Form/Input',
  tags: ['autodocs'],
  render: ({ error, label, description, helperText, ...args }) =>
    createSingleFieldWithMeta(createInput(args), {
      error,
      label,
      description,
      helperText
    }),
  argTypes: {
    fullWidth: { control: 'boolean' },
    error: { control: 'boolean' },
    label: { control: 'text' },
    helperText: { control: 'text' },
    description: { control: 'text' },
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
    type: 'text',
    label: 'Your name'
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
