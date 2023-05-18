import type { StoryObj, Meta } from '@storybook/html'
import type { Props } from './Icon'
import { createIcon } from './Icon'

const meta = {
  title: 'ETF/Icon',
  tags: ['autodocs'],
  render: (args) => {
    return createIcon(args)
  },
  argTypes: {
    key: {
      table: { disable: true }
    },
    color: {
      name: 'color',
      control: { type: 'color' }
    },
    size: {
      name: 'size',
      description: 'Size which maintans the ratio',
      control: { type: 'range', min: 0, max: 500 }
    }
  },
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=5-172&t=NMzWF77GnAa7BvPp-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const Add: Story = {
  args: {
    key: 'add'
  }
}
export const ArrowDown: Story = {
  args: {
    key: 'arrow-down'
  }
}
export const ArrowUp: Story = {
  args: {
    key: 'arrow-up'
  }
}
export const Calendar: Story = {
  args: {
    key: 'calendar'
  }
}
export const ChevronDown: Story = {
  args: {
    key: 'chevron-down'
  }
}
export const Crest: Story = {
  args: {
    key: 'crest'
  }
}
export const Cross: Story = {
  args: {
    key: 'cross'
  }
}
export const Error: Story = {
  args: {
    key: 'error'
  }
}
export const Help: Story = {
  args: {
    key: 'help'
  }
}
export const Logo: Story = {
  args: {
    key: 'logo'
  }
}
export const Menu: Story = {
  args: {
    key: 'menu'
  }
}
export const NewTab: Story = {
  args: {
    key: 'new-tab'
  }
}
export const Pencil: Story = {
  args: {
    key: 'pencil'
  }
}
export const Search: Story = {
  args: {
    key: 'search'
  }
}
export const Success: Story = {
  args: {
    key: 'success'
  }
}
export const Tick: Story = {
  args: {
    key: 'tick'
  }
}
export const Warning: Story = {
  args: {
    key: 'warning'
  }
}
