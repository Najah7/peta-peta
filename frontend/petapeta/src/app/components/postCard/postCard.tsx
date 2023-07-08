"use client";
import { useState, useEffect} from 'react';
import { useRouter } from 'next/router';
import  styles from './postCard.module.css'
import Image from 'next/image'
import { User } from '../../types/user';


const PostCard: React.FC<{ post: Post, user: User }> = ({ post, user }: { post: Post, user: User }): JSX.Element => {
    const { postId, title, imgUrl, comment, createdAt, updatedAt } = post;
    const { userId, userName, iconImgUrl } = user;

    
    const [ isResponsive, setIsResponsive ] = useState<boolean>(false);

    const [windowWidth, setWindowWidth] = useState<number>(window.innerWidth);


    useEffect(() => {
        const handleResize = () => {
          setWindowWidth(window.innerWidth);
          
        };
    
        window.addEventListener('resize', handleResize);
    
        return () => {
          window.removeEventListener('resize', handleResize);
        };
      }, []);

    // const router = useRouter();
    // const handleClick = () => {
    //     router.push(`/post/${postId}`);
    // };
    
    return (
        <section className={styles.card} >
            <div className={styles.card_header}>
                <div className={styles.icon}>
                    <Image src={iconImgUrl} alt="" width={50} height={50}  />
                    <p>{userName}</p>
                </div>
                <div className={styles.post_info}>
                    <h2 className="title">{title}</h2>
                    <div className="dateInfo">
                         <p>created at: {createdAt}</p>
                    </div>
                </div>
            </div>
            
            <div className={styles.main_visual}>
                <Image src={imgUrl[0]} alt="" width={isResponsive? (windowWidth - 100) : 470} height={400} />
            </div>

            <div className={styles.comment}>
                <p className="comment">{comment}</p>
            </div>
        </section>
    );
    }

export default PostCard;