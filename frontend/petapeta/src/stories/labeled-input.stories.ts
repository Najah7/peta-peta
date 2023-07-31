import type { Meta, StoryObj } from '@storybook/react';
import { LabeledInput } from '../app/molecules/labeled-input';

const meta = {
    title: 'Labeled  Input',
    component: LabeledInput,
    tags: ['autodocs'],
} satisfies Meta<typeof LabeledInput>;

export default meta;

type Story = StoryObj<typeof meta>;

export const Default: Story = {
    args: {
        label: 'Label',
    },
};

export const WithPlaceholder: Story = {
    args: {
        label: 'Label',
        placeholder: 'Placeholder',
    },
};

export const WithValue: Story = {
    args: {
        label: 'Label',
        value: 'Value',
    },
};

export const WithMinRows10: Story = {
    args: {
        label: 'Label',
        minRows: 10,
    },
};





