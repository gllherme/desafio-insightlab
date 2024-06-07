"use client";

import { ChangeEvent, useState, MouseEvent } from "react";
import styles from "./autocomplete.module.css";

interface Props {
  suggestions: Array<string>;
  placeholder?: string;
}

export default function Autocomplete({
  suggestions,
  placeholder = "Pesquisar",
}: Props) {
  const [filteredSuggestions, setFilteredSuggestions] = useState<string[]>([]);
  const [activeSuggestion, setActiveSuggestion] = useState<number>(0);
  const [showSuggestions, setShowSuggestions] = useState<boolean>(false);
  const [input, setInput] = useState<string>("");

  const onChange = (event: ChangeEvent<HTMLInputElement>) => {
    const userInput = event.target.value;

    const unlinked = suggestions.filter(
      (suggestion) =>
        suggestion.toLowerCase().indexOf(userInput.toLowerCase()) > -1
    );

    setInput(event.target.value);
    setFilteredSuggestions(unlinked);
    setActiveSuggestion(0);
    setShowSuggestions(true);
  };

  const onClick = (event: MouseEvent) => {
    const target = event.target as HTMLInputElement;
    setFilteredSuggestions([]);
    setInput(target.innerText);
    setActiveSuggestion(0);
    setShowSuggestions(false);
  };

  const SuggestionList = () => {
    return filteredSuggestions.length ? (
      <ul className={styles.list}>
        {filteredSuggestions.map((suggestion, index) => {
          let className;
          if (index === activeSuggestion) {
            className = "suggestionActive";
          }
          return (
            <li className={className} key={suggestion} onClick={onClick}>
              {suggestion}
            </li>
          );
        })}
      </ul>
    ) : (
      <div>
        <em>Sem sugestões</em>
      </div>
    );
  };

  return (
    <>
      <input
        className={styles.input}
        type="text"
        placeholder={placeholder}
        value={input}
        onChange={onChange}
      />
      {showSuggestions && input && <SuggestionList />}
    </>
  );
}
