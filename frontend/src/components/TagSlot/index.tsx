import React from "react";
import styles from "./tagslot.module.css";
import Tag from "../Tag";

interface TagSlotProps {
  tags: Array<string>;
}

export default function TagSlot({ tags }: TagSlotProps) {
  return (
    <div className={styles.slot}>
      {tags.map((tag) => (
        <Tag content={tag} />
      ))}
    </div>
  );
}
