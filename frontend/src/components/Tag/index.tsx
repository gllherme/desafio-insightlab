import styles from "./tag.module.css";

interface TagProps {
  content: string;
}

export default function Tag({ content }: TagProps) {
  return <span className={styles.tag}>{content}</span>;
}
