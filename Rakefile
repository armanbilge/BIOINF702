task 'assignment1' => 'assignment1.pdf'
rule '.pdf' => '.md' do |t|
  sh "pandoc #{t.source} -o #{t.name}"
end
