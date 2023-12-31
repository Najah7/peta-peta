"use client";
import { Box } from "@chakra-ui/react";

type StickeysProps = {
  top: number;
  left: number;
  comment: string;
};
function Stickeys(props: StickeysProps) {
  return (
    <>
      <Box
        w="100px"
        h="100px"
        bg="#ec7b26"
        position="absolute"
        top={props.top}
        left={props.left}
        p="10px"
        borderRadius="20px"
        opacity="0.8"
      ><div style={{
        text-stroke
        position: "absolute",
        width: "100vw",
        height: "100%",
        opacity: 0,
        
      }}>
        {props.comment}
        </div>
      </Box>
    </>
  );
}

export default Stickeys;
