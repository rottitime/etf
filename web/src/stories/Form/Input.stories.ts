import type { StoryObj, Meta } from '@storybook/html'
import { createInput, createSingleFieldWithMeta, FieldMeta, Input } from '../utils'

type Props = Input & FieldMeta

/**
 * Standard input field
 * ##When to use this component
 * If you need users to input short text such as their name or phone number that doesn't exceed a single line, then you should opt for the text input component.
 * ##How it works
 * You should have labels for all text inputs, and generally, it's recommended to keep them visible. Labels should be positioned above the respective text input and must be concise, straightforward, and written in sentence case. Avoid using colons at the end of the labels.
 *
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
    placeholder: {
      control: 'text',
      description:
        'Lower color contrast and disappears when users start writing in the field. But if the text contains instructional info or examples which vanish, it can hinder users from confirming their responses before submitting the form.'
    },
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

export const Search: Story = {
  args: {
    className: 'search-icon',
    placeholder: 'Search keywords...',
    fullWidth: true
  }
}

export const Error: Story = {
  args: {
    ...Description.args,
    error: true
  }
}
