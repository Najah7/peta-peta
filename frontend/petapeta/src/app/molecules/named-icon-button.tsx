import React from "react";
import { Button, Typography } from "@mui/material";
import Image from "next/image";

interface Props {
    text: string;
    iconUrl?: string;
    size?: number;
    onClick?: () => void;
}

export const NamedIconButton: React.FC<Props> = ({
    text='button',
    iconUrl,
    size=24,
    onClick
}): JSX.Element => {

    const styles = {
        root: {
            padding: '5px 10px',
            border: 'none',
            color: 'black',
        },
        icon: {
            width: size,
            height: size,
        },
        text: {
            marginLeft: 10,
        },
    }

    return (
        
        <Button style={styles.root} onClick={onClick}>
            { iconUrl &&
                <Image src={iconUrl} alt='icon' width={size} height={size} />
            }
            <Typography style={styles.text} noWrap>
            {text}
            </Typography>
        </Button>
    )
}

export default NamedIconButton;