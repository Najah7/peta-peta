import React from "react";
import { Avatar, Typography } from "@mui/material";

interface Props {
    name: string;
    avatarUrl?: string;
    size?: number;
    color?: string;
}

export const NamedAvatar: React.FC<Props> = ({ name, avatarUrl='/sample/user/anonymous.jpg', size=50, color='black' }) => {

    const styles: { [key: string]: React.CSSProperties } = {
        root: {
            textAlign: 'center',
            width: '23%', // 4つ並べるために23%にしている。（marginの両端が1%の計算）
            margin: '0 1%',
        },
        avatar: {
            width: size,
            height: size,
            margin: '0 auto',
            border: '1px solid ' + color,
        },
        name: {
            color: color,
        },
    };

    return (
        <div style={styles.root}>
            <Avatar alt={name} src={avatarUrl} style={styles.avatar}/>
            <Typography noWrap style={styles.name}>
                {name}
            </Typography>
        </div>
    );
}

export default NamedAvatar;