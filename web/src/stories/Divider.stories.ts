import type { StoryObj, Meta } from '@storybook/html'

type Props = {
  spacing?: 8 | 16 | 24
}

/**
 * A banner to indicate the current phase of the service.
 */
const meta = {
  title: 'Components/Divider',
  render: ({ spacing }) => {
    const hr = document.createElement('hr')
    if (spacing) hr.classList.add(`my-${spacing}`)
    return hr
  },
  argTypes: {
    spacing: {
      control: { type: 'select' },
      options: [0, 8, 16, 24]
    }
  },
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=38-107&t=5eFOsFvCi3xiEsBW-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const Divider: Story = {
  args: {}
}
