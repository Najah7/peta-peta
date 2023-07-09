"use client";
import { Box, Heading, Input, Spacer } from "@chakra-ui/react";
import Image from "next/image";
import Link from "next/link";
import styles from "./header.module.css";

const Header = () => {
  return (
    <header className="border-b flex items-center h-14 px-4">
      <div className={styles.logo}>
        <Image src="/rogo2.svg" alt="Logo" width={80} height={80} priority />
        <Box m={2} p={2}></Box>
        <Heading fontSize="7xl">PETA</Heading>
        <Box m={1} p={1}></Box>
        <Heading fontSize="7xl">PETA</Heading>
        <Spacer />
        <Input mr="100px" h="40px" w="600px" />
        <Link href="/">
          <Image src="/home2.svg" alt="Logo" width={60} height={60} priority />
        </Link>

        <Box m={1} p={1}></Box>
        <Heading fontSize="4xl">ホーム</Heading>
        <Box m={2} p={2}></Box>
        <Link href="/">
          <Image
            src="/toukou2.svg"
            alt="Logo"
            width={60}
            height={60}
            priority
          />
        </Link>
        <Box m={1} p={1}></Box>
        <Heading fontSize="4xl">投稿</Heading>
      </div>
    </header>
  );
};

export default Header;
