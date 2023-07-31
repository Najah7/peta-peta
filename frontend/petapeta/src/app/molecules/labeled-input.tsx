import  React  from "react";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Typography from "@mui/material/Typography";

interface Props {
    label: string;
    minRows?: number;
    placeholder?: string;
    value?: string;
    onChange?: (event: React.ChangeEvent<HTMLInputElement>) => void;
}

const defaultOnChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    console.log(event.target.value);
}

export const LabeledInput: React.FC<Props> = ({
    label,
    minRows=3,
    placeholder,
    value,
    onChange=defaultOnChange,
}): JSX.Element => {

        const theme = createTheme({
            palette: {
            primary: {
                main: "#ea7b25", // クリック時の色を#ea7b25に指定
            },
            },
        });
    
        return (
            <ThemeProvider theme={theme}>
                <Box >
                <Typography noWrap variant="h5" my={2} ml={1}>
                {label}
                </Typography>
                <TextField
                    multiline
                    value={value}
                    placeholder={placeholder}
                    onChange={onChange}
                    fullWidth
                    minRows={minRows}
                />
                </Box>
            </ThemeProvider>
            
        )
    }