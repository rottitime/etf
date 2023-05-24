import type { StoryObj, Meta } from '@storybook/html'
import { createRadio, createSingleFieldWithMeta, FieldMeta, Radio } from '../utils'

type Props = Radio & FieldMeta

// const list = [...Array(5).keys()].map((i) => `Option ${i}`)

/**
 * Standard input field
 */
const meta = {
  title: 'Components/Form/Radio',
  tags: ['autodocs'],
  render: ({ error, label, description, helperText, ...args }) => {
    return createSingleFieldWithMeta(createRadio({ ...args, text: 'dedede1' }), {
      error,
      label,
      description,
      helperText
    })
  },
  argTypes: {
    error: { control: 'boolean' },
    label: { control: 'text' },
    helperText: { control: 'text' },
    description: { control: 'text' },
    onkeyup: { action: 'changed', table: { disable: true } }
  },
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=32-159&t=s7R0duWzGfG8Vf2S-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const Default: Story = {
  args: {
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
